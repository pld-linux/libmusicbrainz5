Summary:	A software library for accesing MusicBrainz servers
Summary(pl.UTF-8):	Biblioteka umożliwiająca korzystanie z serwerów MusicBrainz
Name:		libmusicbrainz5
Version:	5.1.0
Release:	3
License:	LGPL v2.1
Group:		Libraries
#Source0Download: https://github.com/metabrainz/libmusicbrainz/releases
Source0:	https://github.com/metabrainz/libmusicbrainz/releases/download/release-%{version}/libmusicbrainz-%{version}.tar.gz
# Source0-md5:	4cc5556aa40ff7ab8f8cb83965535bc3
URL:		http://musicbrainz.org/doc/libmusicbrainz/
BuildRequires:	cmake >= 2.6
BuildRequires:	neon-devel >= 0.25
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.604
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The MusicBrainz client library allows applications to make metadata
lookup to a MusicBrainz server, generate signatures from WAV data and
create CD Index Disk ids from audio CD roms.

%description -l pl.UTF-8
Biblioteka kliencka MusicBrainz pozwala aplikacjom na wysyłanie
zapytań do serwerów MusicBrainz, generowanie sygnatur z plików WAV
oraz tworzenie indeksów z płyt CD audio.

%package devel
Summary:	Headers for developing programs that will use libmusicbrainz
Summary(pl.UTF-8):	Pliki nagłówkowe do rozwijania programów używających libmusicbrainz
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel
Requires:	libxml2-devel >= 2.0
Requires:	neon-devel >= 0.25

%description devel
This package contains the headers that programmers will need to
develop applications which will use libmusicbrainz.

%description devel -l pl.UTF-8
Pliki nagłówkowe potrzebne programistom do rozwijania aplikacji
używających biblioteki libmusicbrainz.

%prep
%setup -q -n libmusicbrainz-%{version}

%build
%cmake .

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS.txt NEWS.txt README.md
%attr(755,root,root) %{_libdir}/libmusicbrainz5.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmusicbrainz5.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmusicbrainz5.so
%{_includedir}/musicbrainz5
%{_pkgconfigdir}/libmusicbrainz5.pc
