Summary:	Contacts manager for GNOME
Name:		gnome-contacts
Version:	3.2.2
Release:	1
License:	GPL v2+
Group:		Applications/Communications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-contacts/3.2/%{name}-%{version}.tar.xz
# Source0-md5:	b7974ffcdd106fe9c42a074c465d0ef0
URL:		https://live.gnome.org/ThreePointOne/Features/Contacts
BuildRequires:	autoconf >= 2.67
BuildRequires:	automake
BuildRequires:	evolution-data-server-devel >= 3.2.0
BuildRequires:	folks-devel >= 0.6.1.1
BuildRequires:	glib2-devel >= 1:2.30.0
BuildRequires:	gnome-desktop-devel >= 3.2.0
BuildRequires:	gnome-online-accounts-devel
BuildRequires:	gtk+3-devel
BuildRequires:	intltool
BuildRequires:	libnotify-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 2:0.14.0
BuildRequires:	xz
Requires:	evolution-data-server >= 3.2.0
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
