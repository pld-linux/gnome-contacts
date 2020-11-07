#
# Conditional build:
%bcond_with	telepathy	# Telepathy call/chat support (broken as of 3.36.1-3.38)

Summary:	Contacts manager for GNOME
Summary(pl.UTF-8):	Zarządca kontaktów dla GNOME
Name:		gnome-contacts
Version:	3.38.1
Release:	1
License:	GPL v2+
Group:		Applications/Communications
Source0:	https://download.gnome.org/sources/gnome-contacts/3.38/%{name}-%{version}.tar.xz
# Source0-md5:	2b88637aa758d4df2a3754ca18c82d41
URL:		https://wiki.gnome.org/Apps/Contacts
BuildRequires:	cheese-devel >= 3.4.0
BuildRequires:	clutter-gtk-devel
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	evolution-data-server-devel >= 3.30
BuildRequires:	folks-devel >= 0.14
BuildRequires:	gettext-tools >= 0.17
BuildRequires:	glib2-devel >= 1:2.58
BuildRequires:	gnome-desktop-devel >= 3.2.0
BuildRequires:	gnome-online-accounts-devel
BuildRequires:	gtk+3-devel >= 3.23.1
BuildRequires:	libgee-devel >= 0.10.0
BuildRequires:	libhandy1-devel >= 1.0.0
BuildRequires:	libxslt-progs
BuildRequires:	meson >= 0.50
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
%{?with_telepathy:BuildRequires:	telepathy-glib-devel >= 0.22.0}
BuildRequires:	vala >= 2:0.40.10
BuildRequires:	vala-evolution-data-server >= 3.30
BuildRequires:	vala-folks >= 0.14
BuildRequires:	vala-gnome-online-accounts
BuildRequires:	vala-libhandy1 >= 1.0.0
%{?with_telepathy:BuildRequires:	vala-telepathy-glib >= 0.22.0}
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.58
Requires(post,postun):	gtk-update-icon-cache
Requires:	cheese >= 3.4.0
Requires:	evolution-data-server >= 3.30
Requires:	folks >= 0.14
Requires:	glib2 >= 1:2.58
Requires:	gnome-desktop >= 3.2.0
Requires:	gtk+3 >= 3.23.1
Requires:	libhandy1 >= 1.0.0
%{?with_telepathy:Requires:	telepathy-glib >= 0.22.0}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gnome-contacts is a standalone contacts manager for GNOME desktop.

%description -l pl.UTF-8
gnome-contacts to samodzielny zarządca kontaktów dla środowiska GNOME.

%prep
%setup -q

%build
%meson build \
	%{?with_telepathy:-Dtelepathy=true}

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
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Contacts.Devel.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Contacts-symbolic.svg
%{_mandir}/man1/gnome-contacts.1*
