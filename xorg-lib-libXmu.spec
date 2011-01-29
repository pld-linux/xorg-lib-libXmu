Summary:	X Miscellaneous Utilities library
Summary(pl.UTF-8):	Biblioteka różnych funkcji użytkowych X
Name:		xorg-lib-libXmu
Version:	1.1.0
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXmu-%{version}.tar.bz2
# Source0-md5:	6836883a0120e8346cf7f58dc42e465a
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	docbook-dtd43-xml
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xmlto >= 0.0.20
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-lib-xtrans-devel
BuildRequires:	xorg-sgml-doctools >= 1.5
BuildRequires:	xorg-util-util-macros >= 1.10
Obsoletes:	libXmu
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
Requires:	xorg-lib-libXt-devel
Obsoletes:	libXmu-devel

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
Obsoletes:	libXmu-static

%description static
X Miscellaneous Utilities library.

This package contains the static libXmu library.

%description static -l pl.UTF-8
Biblioteka różnych funkcji użytkowych X (X Miscellaneous Utilities).

Pakiet zawiera statyczną bibliotekę libXmu.

%prep
%setup -q -n libXmu-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README doc/*.{html,css}
%attr(755,root,root) %{_libdir}/libXmu.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libXmu.so.6
%attr(755,root,root) %{_libdir}/libXmuu.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libXmuu.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXmu.so
%attr(755,root,root) %{_libdir}/libXmuu.so
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
