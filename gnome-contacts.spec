Summary:	Contacts manager for GNOME
Summary(pl.UTF-8):	Zarządca kontaktów dla GNOME
Name:		gnome-contacts
Version:	3.34.1
Release:	1
License:	GPL v2+
Group:		Applications/Communications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-contacts/3.34/%{name}-%{version}.tar.xz
# Source0-md5:	fc46610d2a4a5ee476441897ea9d94dc
URL:		https://wiki.gnome.org/Apps/Contacts
BuildRequires:	cheese-devel >= 3.4.0
BuildRequires:	clutter-gtk-devel
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	evolution-data-server-devel >= 3.13.90
BuildRequires:	folks-devel >= 0.11.4
BuildRequires:	gettext-tools >= 0.17
BuildRequires:	glib2-devel >= 1:2.44.0
BuildRequires:	gnome-desktop-devel >= 3.2.0
BuildRequires:	gnome-online-accounts-devel
BuildRequires:	gtk+3-devel >= 3.23.1
BuildRequires:	libgee-devel >= 0.10.0
BuildRequires:	libhandy-devel >= 0.0.9
BuildRequires:	libxslt-progs
BuildRequires:	meson >= 0.41
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	telepathy-glib-devel >= 0.22.0
BuildRequires:	vala >= 2:0.24.0
BuildRequires:	vala-evolution-data-server
BuildRequires:	vala-folks
BuildRequires:	vala-gnome-online-accounts
BuildRequires:	vala-libhandy >= 0.0.9
BuildRequires:	vala-telepathy-glib >= 0.22.0
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.44.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	cheese >= 3.4.0
Requires:	evolution-data-server >= 3.13.90
Requires:	folks >= 0.11.4
Requires:	glib2 >= 1:2.44.0
Requires:	gnome-desktop >= 3.2.0
Requires:	gtk+3 >= 3.23.1
Requires:	libhandy >= 0.0.9
Requires:	telepathy-glib >= 0.22.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gnome-contacts is a standalone contacts manager for GNOME desktop.

%description -l pl.UTF-8
gnome-contacts to samodzielny zarządca kontaktów dla środowiska GNOME.

%prep
%setup -q

%build
%meson build \
	-Dtelepathy=true

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README.md NEWS
%attr(755,root,root) %{_bindir}/gnome-contacts
%attr(755,root,root) %{_libexecdir}/gnome-contacts-search-provider
%{_datadir}/dbus-1/services/org.gnome.Contacts.service
%{_datadir}/dbus-1/services/org.gnome.Contacts.SearchProvider.service
%{_datadir}/glib-2.0/schemas/org.gnome.Contacts.gschema.xml
%{_datadir}/gnome-shell/search-providers/org.gnome.Contacts.search-provider.ini
%{_datadir}/metainfo/org.gnome.Contacts.appdata.xml
%{_desktopdir}/org.gnome.Contacts.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Contacts.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Contacts-symbolic.svg
%{_mandir}/man1/gnome-contacts.1*
