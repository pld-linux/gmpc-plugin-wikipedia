%define		source_name gmpc-wikipedia
Summary:	Wikipedia plugin for Gnome Music Player Client
Summary(pl.UTF-8):	Wtyczka wikipedia dla odtwarzacza Gnome Music Player Client
Name:		gmpc-plugin-wikipedia
Version:	11.8.16
Release:	2
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://download.sarine.nl/Programs/gmpc/%{version}/%{source_name}-%{version}.tar.gz
# Source0-md5:	b8eb533fd2eb531f8e99da3228811b4f
URL:		http://gmpc.wikia.com/wiki/GMPC_PLUGIN_WIKIPEDIA
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gmpc-devel >= 0.19.0
BuildRequires:	gtk+2-devel >= 2:2.4
BuildRequires:	gtk-webkit-devel
BuildRequires:	intltool
BuildRequires:	libmpd-devel >= 0.19.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
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
