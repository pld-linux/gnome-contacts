# TODO: use gtk4-update-icon-cache
Summary:	Contacts manager for GNOME
Summary(pl.UTF-8):	Zarządca kontaktów dla GNOME
Name:		gnome-contacts
Version:	46.0
Release:	1
License:	GPL v2+
Group:		Applications/Communications
Source0:	https://download.gnome.org/sources/gnome-contacts/46/%{name}-%{version}.tar.xz
# Source0-md5:	663d4798f467f83ce82e4f4a4c096d52
Patch0:		%{name}-no-update.patch
URL:		https://wiki.gnome.org/Apps/Contacts
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	evolution-data-server-devel >= 3.42
BuildRequires:	folks-devel >= 0.14
BuildRequires:	gettext-tools >= 0.17
BuildRequires:	glib2-devel >= 1:2.64
BuildRequires:	gnome-online-accounts-devel
BuildRequires:	gtk4-devel >= 4.12
BuildRequires:	libadwaita-devel >= 1.4
BuildRequires:	libgee-devel >= 0.10.0
BuildRequires:	libportal-gtk4-devel >= 0.6
BuildRequires:	libxslt-progs
BuildRequires:	meson >= 0.59
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	qrencode-devel >= 4.1.1
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 2:0.56.11
BuildRequires:	vala-evolution-data-server >= 3.42
BuildRequires:	vala-folks >= 0.14
BuildRequires:	vala-gnome-online-accounts
BuildRequires:	vala-libadwaita >= 1.4
BuildRequires:	vala-libgee >= 0.10.0
BuildRequires:	vala-libportal-gtk4 >= 0.6
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.64
Requires(post,postun):	gtk-update-icon-cache
Requires:	evolution-data-server >= 3.42
Requires:	folks >= 0.14
Requires:	glib2 >= 1:2.64
Requires:	gtk4 >= 4.12
Requires:	libadwaita >= 1.4
Requires:	libportal >= 0.5
Requires:	qrencode-libs >= 4.1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gnome-contacts is a standalone contacts manager for GNOME desktop.

%description -l pl.UTF-8
gnome-contacts to samodzielny zarządca kontaktów dla środowiska GNOME.

%prep
%setup -q
%patch0 -p1

%build
%meson build

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
%doc README.md
%attr(755,root,root) %{_bindir}/gnome-contacts
%attr(755,root,root) %{_libexecdir}/gnome-contacts-search-provider
%dir %{_libexecdir}/gnome-contacts
%attr(755,root,root) %{_libexecdir}/gnome-contacts/gnome-contacts-parser
%{_datadir}/dbus-1/services/org.gnome.Contacts.service
%{_datadir}/dbus-1/services/org.gnome.Contacts.SearchProvider.service
%{_datadir}/glib-2.0/schemas/org.gnome.Contacts.gschema.xml
%{_datadir}/gnome-shell/search-providers/org.gnome.Contacts.search-provider.ini
%{_datadir}/metainfo/org.gnome.Contacts.appdata.xml
%{_desktopdir}/org.gnome.Contacts.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Contacts.svg
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Contacts.Devel.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Contacts-symbolic.svg
%{_mandir}/man1/gnome-contacts.1*
