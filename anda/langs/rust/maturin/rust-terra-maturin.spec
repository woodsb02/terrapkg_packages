# Generated by rust2rpm 26
%global crate maturin

Name:           rust-terra-maturin
Version:        1.7.1
Release:        1%?dist
Summary:        Build and publish crates with pyo3, rust-cpython and cffi bindings as well as rust binaries as python packages

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/maturin
Source:         %{crates_source}

BuildRequires:  pkgconfig anda-srpm-macros cargo-rpm-macros >= 24
Conflicts:      rust-maturin

%global _description %{expand:
Build and publish crates with pyo3, rust-cpython and cffi bindings as
well as rust binaries as python packages.}

%description %{_description}

%package     -n terra-%{crate}
Summary:        %{summary}
Conflicts:      %crate

%description -n terra-%{crate} %{_description}

%files       -n terra-%{crate}
%license license-apache
%license license-mit
%doc Changelog.md
%doc README.md
%{_bindir}/maturin

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+bytesize-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+bytesize-devel %{_description}

This package contains library source intended for building other packages which
use the "bytesize" feature of the "%{crate}" crate.

%files       -n %{name}+bytesize-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+cargo-xwin-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+cargo-xwin-devel %{_description}

This package contains library source intended for building other packages which
use the "cargo-xwin" feature of the "%{crate}" crate.

%files       -n %{name}+cargo-xwin-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+cargo-zigbuild-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+cargo-zigbuild-devel %{_description}

This package contains library source intended for building other packages which
use the "cargo-zigbuild" feature of the "%{crate}" crate.

%files       -n %{name}+cargo-zigbuild-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+cli-completion-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+cli-completion-devel %{_description}

This package contains library source intended for building other packages which
use the "cli-completion" feature of the "%{crate}" crate.

%files       -n %{name}+cli-completion-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+configparser-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+configparser-devel %{_description}

This package contains library source intended for building other packages which
use the "configparser" feature of the "%{crate}" crate.

%files       -n %{name}+configparser-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+console-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+console-devel %{_description}

This package contains library source intended for building other packages which
use the "console" feature of the "%{crate}" crate.

%files       -n %{name}+console-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+cross-compile-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+cross-compile-devel %{_description}

This package contains library source intended for building other packages which
use the "cross-compile" feature of the "%{crate}" crate.

%files       -n %{name}+cross-compile-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+dialoguer-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dialoguer-devel %{_description}

This package contains library source intended for building other packages which
use the "dialoguer" feature of the "%{crate}" crate.

%files       -n %{name}+dialoguer-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+faster-tests-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+faster-tests-devel %{_description}

This package contains library source intended for building other packages which
use the "faster-tests" feature of the "%{crate}" crate.

%files       -n %{name}+faster-tests-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+full-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+full-devel %{_description}

This package contains library source intended for building other packages which
use the "full" feature of the "%{crate}" crate.

%files       -n %{name}+full-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+human-panic-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+human-panic-devel %{_description}

This package contains library source intended for building other packages which
use the "human-panic" feature of the "%{crate}" crate.

%files       -n %{name}+human-panic-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+keyring-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+keyring-devel %{_description}

This package contains library source intended for building other packages which
use the "keyring" feature of the "%{crate}" crate.

%files       -n %{name}+keyring-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+log-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+log-devel %{_description}

This package contains library source intended for building other packages which
use the "log" feature of the "%{crate}" crate.

%files       -n %{name}+log-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+minijinja-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+minijinja-devel %{_description}

This package contains library source intended for building other packages which
use the "minijinja" feature of the "%{crate}" crate.

%files       -n %{name}+minijinja-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+multipart-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+multipart-devel %{_description}

This package contains library source intended for building other packages which
use the "multipart" feature of the "%{crate}" crate.

%files       -n %{name}+multipart-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+native-tls-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+native-tls-devel %{_description}

This package contains library source intended for building other packages which
use the "native-tls" feature of the "%{crate}" crate.

%files       -n %{name}+native-tls-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+password-storage-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+password-storage-devel %{_description}

This package contains library source intended for building other packages which
use the "password-storage" feature of the "%{crate}" crate.

%files       -n %{name}+password-storage-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+rustls-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rustls-devel %{_description}

This package contains library source intended for building other packages which
use the "rustls" feature of the "%{crate}" crate.

%files       -n %{name}+rustls-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+scaffolding-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+scaffolding-devel %{_description}

This package contains library source intended for building other packages which
use the "scaffolding" feature of the "%{crate}" crate.

%files       -n %{name}+scaffolding-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+tracing-subscriber-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tracing-subscriber-devel %{_description}

This package contains library source intended for building other packages which
use the "tracing-subscriber" feature of the "%{crate}" crate.

%files       -n %{name}+tracing-subscriber-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unicode-xid-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unicode-xid-devel %{_description}

This package contains library source intended for building other packages which
use the "unicode-xid" feature of the "%{crate}" crate.

%files       -n %{name}+unicode-xid-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+upload-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+upload-devel %{_description}

This package contains library source intended for building other packages which
use the "upload" feature of the "%{crate}" crate.

%files       -n %{name}+upload-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+ureq-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+ureq-devel %{_description}

This package contains library source intended for building other packages which
use the "ureq" feature of the "%{crate}" crate.

%files       -n %{name}+ureq-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+wild-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+wild-devel %{_description}

This package contains library source intended for building other packages which
use the "wild" feature of the "%{crate}" crate.

%files       -n %{name}+wild-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+xwin-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+xwin-devel %{_description}

This package contains library source intended for building other packages which
use the "xwin" feature of the "%{crate}" crate.

%files       -n %{name}+xwin-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+zig-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+zig-devel %{_description}

This package contains library source intended for building other packages which
use the "zig" feature of the "%{crate}" crate.

%files       -n %{name}+zig-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep_online

%build
cargo add time -F macros
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
