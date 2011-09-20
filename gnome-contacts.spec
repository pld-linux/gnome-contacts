Summary:	Contacts manager for GNOME
Name:		gnome-contacts
Version:	0.1.5.2
Release:	1
License:	GPL v2+
Group:		Applications/Communications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-contacts/0.1/%{name}-%{version}.tar.xz
# Source0-md5:	5eb2f9e3f11347500c16b12777cd020b
URL:		https://live.gnome.org/ThreePointOne/Features/Contacts
BuildRequires:	autoconf >= 2.67
BuildRequires:	automake
BuildRequires:	folks-devel >= 0.6.1.1
BuildRequires:	glib2-devel >= 1:2.29.12
BuildRequires:	gnome-desktop-devel >= 3.0
BuildRequires:	gnome-online-accounts-devel
BuildRequires:	gtk+3-devel
BuildRequires:	intltool
BuildRequires:	libnotify-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 1:0.14.0
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gnome-contacts is a standalone contacts manager for GNOME desktop.

%prep
%setup -q

%build
mkdir m4
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README NEWS TODO ChangeLog
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
