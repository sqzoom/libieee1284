Summary:	A library for interfacing IEEE 1284-compatible devices
Summary(pl):	Biblioteka do komunikacji z urządzeniami kompatybilnymi z IEEE 1284
Name:		libieee1284
Version:	0.2.9
%define		_pre pre2
Release:	0.%{_pre}.1
License:	GPL
Group:		Libraries
Source0:	http://cyberelk.net/tim/data/libieee1284/stable/%{name}-%{version}%{_pre}.tar.bz2
# Source0-md5:	d9682040b3cb3bf8ece7f104cbb11dcd
URL:		http://cyberelk.net/tim/libieee1284/index.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	docbook-dtd41-sgml
BuildRequires:	docbook-utils
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libieee1284 library is for communicating with parallel port
devices.

%description -l pl
Biblioteka libieee1284 służy do komunikacji z urządzeniami
podłączanymi do portu równoległego.

%package devel
Summary:	Files for developing applications that use libieee1284
Summary(pl):	Pliki do tworzenia programów używających libieee1284
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
The header files, libtool library and man pages for developing
applications that use libieee1284.

%description devel -l pl
Pliki nagłówkowe i dokumentacja do tworzenia programów używających
libieee1284.

%package static
Summary:	Static version of libieee1284
Summary(pl):	Statyczna wersja libieee1284
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static version of libieee1284 library.

%description static -l pl
Statyczna wersja biblioteki libieee1284.

%prep
%setup -q -n %{name}-%{version}%{_pre}

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/libieee1284_test
%attr(755,root,root) %{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/ieee1284.h
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_mandir}/man?/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
