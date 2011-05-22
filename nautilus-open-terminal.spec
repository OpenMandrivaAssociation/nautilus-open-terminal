%define name nautilus-open-terminal
%define version 0.18
%define release %mkrel 4

Summary: Open a terminal in a specified folder
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
License: GPLv2+
Group: Graphical desktop/GNOME
Url: http://www.gnome-de.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: nautilus-devel >= 2.21.2
BuildRequires: gnome-desktop-devel >= 2.9.91
BuildRequires: intltool

%description
This is a proof-of-concept Nautilus extension which allows you to open
a terminal in arbitrary local folders.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT %name.lang
%makeinstall_std
%find_lang %name
rm -f %buildroot%_libdir/nautilus/extensions-*/libnautilus-open-terminal.*a

%clean
rm -rf $RPM_BUILD_ROOT

%post
%post_install_gconf_schemas %name
%preun
%preun_uninstall_gconf_schemas %name

%files -f %name.lang
%defattr(-,root,root)
%doc ChangeLog NEWS README AUTHORS TODO
%_sysconfdir/gconf/schemas/%name.schemas
%_libdir/nautilus/extensions-2.0/libnautilus-open-terminal.so


