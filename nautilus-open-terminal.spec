Summary: Open a terminal in a specified folder
Name:    nautilus-open-terminal
Version: 0.19
Release: 2
Source0: http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
License: GPLv2+
Group: Graphical desktop/GNOME
Url: https://www.gnome-de.org
BuildRequires: nautilus-devel >= 2.21.2
BuildRequires: intltool
BuildRequires: pkgconfig(gnome-desktop-3.0)
BuildRequires: pkgconfig(gconf-2.0)

%description
This is a proof-of-concept Nautilus extension which allows you to open
a terminal in arbitrary local folders.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std
%find_lang %name
rm -f %buildroot%_libdir/nautilus/extensions-*/libnautilus-open-terminal.*a

%preun
%preun_uninstall_gconf_schemas %name

%files -f %name.lang
%doc ChangeLog NEWS README AUTHORS TODO
%_sysconfdir/gconf/schemas/%name.schemas
%_libdir/nautilus/extensions-3.0/libnautilus-open-terminal.so
