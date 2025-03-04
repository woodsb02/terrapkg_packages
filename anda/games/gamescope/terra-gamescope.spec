%if 0%{?fedora} >= 41
%global libliftoff_minver 0.5.0
%else
%global libliftoff_minver 0.4.1
%endif

%global toolchain clang
%global _default_patch_fuzz 2
%global gamescope_tag 3.15.9

Name:           terra-gamescope
Version:        100.%{gamescope_tag}
Release:        1%?dist
Summary:        Micro-compositor for video games on Wayland - Terra patch, please read the full description

License:        BSD
URL:            https://github.com/ValveSoftware/gamescope

# Create stb.pc to satisfy dependency('stb')
Source0:        stb.pc
Source1:        gamescope-legacy.sh

Patch0:         0001-cstdint.patch

# https://github.com/ChimeraOS/gamescope
Patch1:         chimeraos.patch
# https://hhd.dev/
Patch2:         disable-steam-touch-click-atom.patch
Patch3:         v2-0001-always-send-ctrl-1-2-to-steam-s-wayland-session.patch

# Set default backend to SDL instead of Wayland, to avoid issues with GPUs that do not support
# Vulkan DRM modifiers.
# See also: gamescope-legacy package
# https://github.com/ValveSoftware/gamescope/issues/1218#issuecomment-2123801764
Patch6:         1483.patch

BuildRequires:  meson >= 0.54.0
BuildRequires:  ninja-build
BuildRequires:  cmake
BuildRequires:  clang
BuildRequires:  glm-devel
BuildRequires:  google-benchmark-devel
BuildRequires:  libXmu-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libeis-devel
BuildRequires:  pixman-devel
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xres)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server) >= 1.23.0
BuildRequires:  pkgconfig(wayland-protocols) >= 1.17
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libavif)
BuildRequires:  pkgconfig(wlroots)
BuildRequires:  pkgconfig(libliftoff) >= 0.4.1
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(hwdata)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  spirv-headers-devel
# Enforce the the minimum EVR to contain fixes for all of:
# CVE-2021-28021 CVE-2021-42715 CVE-2021-42716 CVE-2022-28041 CVE-2023-43898
# CVE-2023-45661 CVE-2023-45662 CVE-2023-45663 CVE-2023-45664 CVE-2023-45666
# CVE-2023-45667
BuildRequires:  stb_image-devel >= 2.28^20231011gitbeebb24-12
# Header-only library: -static is for tracking per guidelines
BuildRequires:  stb_image-static
BuildRequires:  stb_image_resize-devel
BuildRequires:  stb_image_resize-static
BuildRequires:  stb_image_write-devel
BuildRequires:  stb_image_write-static
BuildRequires:  /usr/bin/glslangValidator
BuildRequires:  libdecor-devel
BuildRequires:  libXdamage-devel
BuildRequires:  xorg-x11-server-Xwayland-devel
BuildRequires:  git

# libliftoff hasn't bumped soname, but API/ABI has changed for 0.2.0 release
Requires:       libliftoff%{?_isa} >= %{libliftoff_minver}
Requires:       xorg-x11-server-Xwayland
Requires:       terra-gamescope-libs = %{version}-%{release}
Requires:       terra-gamescope-libs(x86-32) = %{version}-%{release}
Recommends:     mesa-dri-drivers
Recommends:     mesa-vulkan-drivers

Provides:       gamescope-legacy
Obsoletes:      gamescope-legacy < 3.14.2

%description
Gamescope is the micro-compositor optimized for running video games on Wayland.

This specific build of Gamescope is patched to use SDL as the default backend instead of Wayland, and
includes a legacy wrapper script for older GPUs and extra configuration options. Please see
https://developer.fyralabs.com/terra/gamescope for more information.

%package libs
Summary:	libs for Gamescope
%description libs
%summary

%prep
git clone --depth 1 --branch %{gamescope_tag} %{url}.git
cd gamescope
git submodule update --init --recursive
mkdir -p pkgconfig
cp %{SOURCE0} pkgconfig/stb.pc

# Replace spirv-headers include with the system directory
sed -i 's^../thirdparty/SPIRV-Headers/include/spirv/^/usr/include/spirv/^' src/meson.build

%autopatch -p1

%build
cd gamescope
export PKG_CONFIG_PATH=pkgconfig
%if %{__isa_bits} == 64
%meson --auto-features=enabled -Dforce_fallback_for=vkroots,wlroots,libliftoff
%else
%meson -Denable_gamescope=false -Denable_gamescope_wsi_layer=true
%endif
%meson_build

%install
cd gamescope
%meson_install --skip-subprojects

%if %{__isa_bits} == 64
install -Dm755 %{SOURCE1} %{buildroot}%{_bindir}/gamescope-legacy
%endif

%files
%license gamescope/LICENSE
%doc gamescope/README.md
%if %{__isa_bits} == 64
%caps(cap_sys_nice=eip) %{_bindir}/gamescope
%{_bindir}/gamescopectl
%{_bindir}/gamescopestream
%{_bindir}/gamescopereaper
%{_bindir}/gamescope-legacy
%endif

%files libs
%{_libdir}/libVkLayer_FROG_gamescope_wsi_*.so
%{_datadir}/vulkan/implicit_layer.d/VkLayer_FROG_gamescope_wsi.*.json

%changelog
%autochangelog
