# TODO:
# - desc

%define		source_name gmpc-wikipedia
Summary:	Wikipedia plugin for Gnome Music Player Client
Summary(pl.UTF-8):Wtyczka wikipedia dla odtwarzacza Gnome Music Player Client
Name:		gmpc-plugin-wikipedia
Version:	0.18.100
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/musicpd/%{source_name}-%{version}.tar.gz
# Source0-md5:	9da599f634378fba6bd151037c2f9090
URL:		http://gmpc.wikia.com/wiki/GMPC_PLUGIN_WIKIPEDIA
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gmpc-devel >= 0.18.100
BuildRequires:	gtk+2-devel >= 2:2.4
BuildRequires:	libmpd-devel >= 0.18.100
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	gtk-webkit-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This GMPC plugin loopup Wikipedia for information about artists.

%prep
%setup -qn %{source_name}-%{version}

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

install -d $RPM_BUILD_ROOT%{_libdir}/gmpc

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/gmpc/plugins/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gmpc/plugins/*.so
%{_datadir}/gmpc/plugins/wikipedia
