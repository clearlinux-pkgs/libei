#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
#
Name     : libei
Version  : 1.0.0
Release  : 1
URL      : https://gitlab.freedesktop.org/libinput/libei/-/archive/1.0.0/libei-1.0.0.tar.gz
Source0  : https://gitlab.freedesktop.org/libinput/libei/-/archive/1.0.0/libei-1.0.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: libei-bin = %{version}-%{release}
Requires: libei-lib = %{version}-%{release}
Requires: libei-license = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : libxkbcommon-dev
BuildRequires : pkgconfig(libevdev)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(systemd)
BuildRequires : pkgconfig(xkbcommon)
BuildRequires : pypi(attrs)
BuildRequires : pypi(jinja2)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
libei
=====
**libei** is a library for Emulated Input, primarily aimed at the Wayland
stack. It provides three parts:
- 🥚 EI (Emulated Input) for the client side (`libei`)
- 🍦 EIS (Emulated Input Server) for the server side (`libeis`)
- 🚌 oeffis is an optional helper library for DBus communication with the
XDG RemoteDesktop portal (`liboeffis`)

%package bin
Summary: bin components for the libei package.
Group: Binaries
Requires: libei-license = %{version}-%{release}

%description bin
bin components for the libei package.


%package dev
Summary: dev components for the libei package.
Group: Development
Requires: libei-lib = %{version}-%{release}
Requires: libei-bin = %{version}-%{release}
Provides: libei-devel = %{version}-%{release}
Requires: libei = %{version}-%{release}

%description dev
dev components for the libei package.


%package lib
Summary: lib components for the libei package.
Group: Libraries
Requires: libei-license = %{version}-%{release}

%description lib
lib components for the libei package.


%package license
Summary: license components for the libei package.
Group: Default

%description license
license components for the libei package.


%prep
%setup -q -n libei-1.0.0
cd %{_builddir}/libei-1.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1686254938
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dtests=disabled  builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs

%install
mkdir -p %{buildroot}/usr/share/package-licenses/libei
cp %{_builddir}/libei-%{version}/COPYING %{buildroot}/usr/share/package-licenses/libei/7e4ccab0b53f2718a855f5488eb152d10ae6ecf9 || :
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ei-debug-events

%files dev
%defattr(-,root,root,-)
/usr/include/libei-1.0/libei.h
/usr/include/libei-1.0/libeis.h
/usr/include/libei-1.0/liboeffis.h
/usr/lib64/libei.so
/usr/lib64/libeis.so
/usr/lib64/liboeffis.so
/usr/lib64/pkgconfig/libei-1.0.pc
/usr/lib64/pkgconfig/libeis-1.0.pc
/usr/lib64/pkgconfig/liboeffis-1.0.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libei.so.1
/usr/lib64/libei.so.1.0.0
/usr/lib64/libeis.so.1
/usr/lib64/libeis.so.1.0.0
/usr/lib64/liboeffis.so.1
/usr/lib64/liboeffis.so.1.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libei/7e4ccab0b53f2718a855f5488eb152d10ae6ecf9
