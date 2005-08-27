Summary:	X Miscellaneous Utilities library
Summary(pl):	Biblioteka ró¿nych funkcji u¿ytkowych X
Name:		xorg-lib-libXmu
Version:	0.99.0
Release:	0.03
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/lib/libXmu-%{version}.tar.bz2
# Source0-md5:	9a4b28aa9c9f27351e9fa53cde344592
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-util-util-macros
Obsoletes:	libXmu
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X Miscellaneous Utilities library.

%description -l pl
Biblioteka ró¿nych funkcji u¿ytkowych X (X Miscellaneous Utilities).

%package devel
Summary:	Header files libXmu development
Summary(pl):	Pliki nag³ówkowe do biblioteki libXmu
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXt-devel
Obsoletes:	libXmu-devel

%description devel
X Miscellaneous Utilities library.

This package contains the header files needed to develop programs that
use these libXmu.

%description devel -l pl
Biblioteka ró¿nych funkcji u¿ytkowych X (X Miscellaneous Utilities).

Pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania programów
u¿ywaj±cych biblioteki libXmu.

%package static
Summary:	Static libXmu libraries
Summary(pl):	Biblioteki statyczne libXmu
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libXmu-static

%description static
X Miscellaneous Utilities library.

This package contains the static libXmu library.

%description static -l pl
Biblioteka ró¿nych funkcji u¿ytkowych X (X Miscellaneous Utilities).

Pakiet zawiera statyczn± bibliotekê libXmu.

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
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_libdir}/libXm*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXm*.so
%{_libdir}/libXm*.la
%{_includedir}/X11/Xmu/*.h
%{_pkgconfigdir}/xm*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libXm*.a
