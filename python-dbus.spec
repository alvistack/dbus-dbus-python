%global debug_package %{nil}

Name: python-dbus
Epoch: 100
Version: 1.2.18
Release: 1%{?dist}
Summary: Python bindings for libdbus
License: MIT
URL: https://gitlab.freedesktop.org/dbus/dbus-python/-/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: autoconf-archive
BuildRequires: automake
BuildRequires: fdupes
BuildRequires: gcc
BuildRequires: libtool
BuildRequires: pkgconfig
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: python-rpm-macros
BuildRequires: python3-cython
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
dbus-python is the original Python binding for dbus, the reference
implementation of the D-Bus protocol.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitearch} -type f -name '*.pyc' -exec rm -rf {} \;
find %{buildroot}%{python3_sitearch} -type f -name '*.la' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitearch}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-dbus-python
Summary: Python bindings for libdbus
Requires: python3
Provides: python3-dbus-python = %{epoch}:%{version}-%{release}
Provides: python3dist(dbus) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-dbus-python = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(dbus) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-dbus-python = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(dbus) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-dbus-python
dbus-python is the original Python binding for dbus, the reference
implementation of the D-Bus protocol.

%files -n python%{python3_version_nodots}-dbus-python
%license COPYING
%{python3_sitearch}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-dbus-python
Summary: Python bindings for libdbus
Requires: python3
Provides: python3-dbus-python = %{epoch}:%{version}-%{release}
Provides: python3dist(dbus) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-dbus-python = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(dbus) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-dbus-python = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(dbus) = %{epoch}:%{version}-%{release}

%description -n python3-dbus-python
dbus-python is the original Python binding for dbus, the reference
implementation of the D-Bus protocol.

%files -n python3-dbus-python
%license COPYING
%{python3_sitearch}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-dbus
Summary: Python bindings for libdbus
Requires: python3
Provides: python3-dbus = %{epoch}:%{version}-%{release}
Provides: python3dist(dbus) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-dbus = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(dbus) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-dbus = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(dbus) = %{epoch}:%{version}-%{release}

%description -n python3-dbus
dbus-python is the original Python binding for dbus, the reference
implementation of the D-Bus protocol.

%files -n python3-dbus
%license COPYING
%{python3_sitearch}/*
%endif

%changelog
