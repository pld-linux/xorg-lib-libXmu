
#
Summary:	X Miscellaneous Utilities library
Summary(pl):	Biblioteka r�nych funkcji u�ytkowych X
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
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/libXmu-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
X Miscellaneous Utilities library.

%description -l pl
Biblioteka r�nych funkcji u�ytkowych X (X Miscellaneous Utilities).


%package devel
Summary:	Header files libXmu development
Summary(pl):	Pliki nag��wkowe do biblioteki libXmu
Group:		X11/Development/Libraries
Requires:	xorg-lib-libXmu = %{version}-%{release}
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXt-devel

%description devel
X Miscellaneous Utilities library.

This package contains the header files needed to develop programs that
use these libXmu.

%description devel -l pl
Biblioteka r�nych funkcji u�ytkowych X (X Miscellaneous Utilities).

Pakiet zawiera pliki nag��wkowe niezb�dne do kompilowania program�w
u�ywaj�cych biblioteki libXmu.


%package static
Summary:	Static libXmu libraries
Summary(pl):	Biblioteki statyczne libXmu
Group:		Development/Libraries
Requires:	xorg-lib-libXmu-devel = %{version}-%{release}

%description static
X Miscellaneous Utilities library.

This package contains the static libXmu library.

%description static -l pl
Biblioteka r�nych funkcji u�ytkowych X (X Miscellaneous Utilities).

Pakiet zawiera statyczn� bibliotek� libXmu.


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
%attr(755,root,wheel) %{_libdir}/libXm*.so.*


%files devel
%defattr(644,root,root,755)
%{_includedir}/X11/Xmu/*.h
%{_libdir}/libXm*.la
%attr(755,root,wheel) %{_libdir}/libXm*.so
%{_pkgconfigdir}/xm*.pc


%files static
%defattr(644,root,root,755)
%{_libdir}/libXm*.a
