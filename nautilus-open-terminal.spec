%define name nautilus-open-terminal
%define version 0.8
%define release %mkrel 1

Summary: Open a terminal in a specified folder
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://download.gnome.org/sources/nautilus-open-terminal/%{name}-%{version}.tar.bz2
License: GPL
Group: Graphical desktop/GNOME
Url: http://www.gnome-de.org
BuildRequires: nautilus-devel
BuildRequires: perl-XML-Parser
#if patched
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
rm -f %buildroot%_libdir/nautilus/extensions-1.0/libnautilus-open-terminal.*a

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc ChangeLog NEWS README AUTHORS TODO
%_libdir/nautilus/extensions-1.0/libnautilus-open-terminal.so


