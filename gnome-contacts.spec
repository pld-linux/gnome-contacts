Summary:	Contacts manager for GNOME
Name:		gnome-contacts
Version:	0.1.2
Release:	1
License:	GPL v2+
Group:		Applications/Communications
Source0:	http://download.gnome.org/sources/gnome-contacts/0.1/%{name}-%{version}.tar.xz
# Source0-md5:	0c44633a0801022050e057e08ceb4980
URL:		https://live.gnome.org/ThreePointOne/Features/Contacts
BuildRequires:	desktop-file-utils
BuildRequires:	folks-devel
BuildRequires:	gtk+3-devel
BuildRequires:	intltool
BuildRequires:	libnotify-devel
BuildRequires:	vala >= 0.13.3

%description
%{name} is a standalone contacts manager for GNOME desktop.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README NEWS TODO ChangeLog
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT
