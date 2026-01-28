Summary:	X Miscellaneous Utilities library
Summary(pl.UTF-8):	Biblioteka różnych funkcji użytkowych X
Name:		xorg-lib-libXmu
Version:	1.3.0
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	https://xorg.freedesktop.org/releases/individual/lib/libXmu-%{version}.tar.xz
# Source0-md5:	532a37254137e9e1827b8eec95e79adf
Patch0:		libXmu-32bit.patch
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.70
BuildRequires:	automake
BuildRequires:	docbook-dtd43-xml
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xmlto >= 0.0.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXt-devel >= 1.1.0
BuildRequires:	xorg-lib-xtrans-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-sgml-doctools >= 1.8
BuildRequires:	xorg-util-util-macros >= 1.12
BuildRequires:	xz
Requires:	xorg-lib-libXt >= 1.1.0
Obsoletes:	libXmu < 6.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X Miscellaneous Utilities library.

%description -l pl.UTF-8
Biblioteka różnych funkcji użytkowych X (X Miscellaneous Utilities).

%package devel
Summary:	Header files for libXmu and libXmuu libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek libXmu i libXmuu
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXt-devel >= 1.1.0
Obsoletes:	libXmu-devel < 6.3

%description devel
X Miscellaneous Utilities library.

This package contains the header files needed to develop programs that
use libXmu or libXmuu.

%description devel -l pl.UTF-8
Biblioteka różnych funkcji użytkowych X (X Miscellaneous Utilities).

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libXmu lub libXmuu.

%package static
Summary:	Static libXmu libraries
Summary(pl.UTF-8):	Biblioteki statyczne libXmu
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libXmu-static < 6.3

%description static
X Miscellaneous Utilities library.

This package contains the static libXmu library.

%description static -l pl.UTF-8
Biblioteka różnych funkcji użytkowych X (X Miscellaneous Utilities).

Pakiet zawiera statyczną bibliotekę libXmu.

%prep
%setup -q -n libXmu-%{version}
%patch -P0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# (.html format) packaged as %doc
%{__rm} $RPM_BUILD_ROOT%{_docdir}/libXmu/{Xmu.*,xlogo.svg}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%{_libdir}/libXmu.so.*.*.*
%ghost %{_libdir}/libXmu.so.6
%{_libdir}/libXmuu.so.*.*.*
%ghost %{_libdir}/libXmuu.so.1

%files devel
%defattr(644,root,root,755)
%doc doc/{Xmu.html,xlogo.svg}
%{_libdir}/libXmu.so
%{_libdir}/libXmuu.so
%{_libdir}/libXmu.la
%{_libdir}/libXmuu.la
%dir %{_includedir}/X11/Xmu
%{_includedir}/X11/Xmu/*.h
%{_pkgconfigdir}/xmu.pc
%{_pkgconfigdir}/xmuu.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libXmu.a
%{_libdir}/libXmuu.a
