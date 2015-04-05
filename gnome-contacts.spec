Summary:	Contacts manager for GNOME
Name:		gnome-contacts
Version:	3.16.0
Release:	2
License:	GPL v2+
Group:		Applications/Communications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-contacts/3.16/%{name}-%{version}.tar.xz
# Source0-md5:	07fa6b11c8ae4ae6c3227fec7bf2eb82
URL:		https://wiki.gnome.org/Apps/Contacts
BuildRequires:	autoconf >= 2.67
BuildRequires:	automake >= 1.12
BuildRequires:	cheese-devel >= 3.4.0
BuildRequires:	clutter-gtk-devel
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	evolution-data-server-devel >= 3.13.90
BuildRequires:	folks-devel >= 0.9.5
BuildRequires:	geocode-glib-devel >= 3.15.3
BuildRequires:	gettext-tools >= 0.17
BuildRequires:	glib2-devel >= 1:2.38.0
BuildRequires:	gnome-desktop-devel >= 3.2.0
BuildRequires:	gnome-online-accounts-devel
BuildRequires:	gtk+3-devel >= 3.12.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libchamplain-devel >= 0.12
BuildRequires:	libgee-devel >= 0.10.0
BuildRequires:	libnotify-devel
BuildRequires:	libtool
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	tar >= 1:1.22
BuildRequires:	telepathy-glib-devel >= 0.17.5
BuildRequires:	vala >= 2:0.24.0
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.38.0
Requires:	evolution-data-server >= 3.13.90
Requires:	gtk+3 >= 3.12.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gnome-contacts is a standalone contacts manager for GNOME desktop.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4 -I libgd
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

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README NEWS ChangeLog
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_libdir}/gnome-contacts-search-provider
%{_datadir}/appdata/org.gnome.Contacts.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.Contacts.SearchProvider.service
%{_datadir}/glib-2.0/schemas/org.gnome.Contacts.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.Contacts.enums.xml
%{_datadir}/gnome-shell/search-providers/org.gnome.Contacts.search-provider.ini
%{_datadir}/dbus-1/services/org.gnome.Contacts.service
%{_desktopdir}/org.gnome.Contacts.desktop
%{_mandir}/man1/gnome-contacts.1*
