Summary:	Myth TV UPnP library based upon GLib/GObject paradigm
Summary(pl.UTF-8):	Biblioteka Myth TV UPnP oparta na paradygmacie GLib/GObject
Name:		gmyth-upnp
Version:	0.7.1
Release:	4
License:	LGPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/gmyth/%{name}-%{version}.tar.gz
# Source0-md5:	f569d565c9cb12d50e88d23a603c7fcb
URL:		http://gmyth.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gmyth-devel >= 0.7.1
BuildRequires:	libtool
BuildRequires:	libupnp-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Myth TV UPnP library based upon GLib/GObject paradigm.

%description -l pl.UTF-8
Biblioteka Myth TV UPnP oparta na paradygmacie GLib/GObject.

%package devel
Summary:	Header files for gmyth library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki gmyth
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	curl-devel
Requires:	glib2-devel >= 2.0
Requires:	libxml2-devel >= 2.0

%description devel
Header files for gmyth library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki gmyth.

%package static
Summary:	Static gmyth library
Summary(pl.UTF-8):	Statyczna biblioteka gmyth
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gmyth library.

%description static -l pl.UTF-8
Statyczna biblioteka gmyth.

%prep
%setup -q

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
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/libgmythupnp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgmythupnp.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgmythupnp.so
%{_libdir}/libgmythupnp.la
%{_includedir}/gmyth-upnp
%{_pkgconfigdir}/gmyth-upnp.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgmythupnp.a
