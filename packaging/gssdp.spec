Name:       gssdp
Summary:    GSSDP implements resource discovery and announcement over SSDP
Version:    0.14.4
Release:    1
Group:      System/Libraries
License: LGPL-2.0+
URL:        http://www.gupnp.org
Source0:    http://download.gnome.org/sources/%{name}/0.14/%{name}-%{version}.tar.bz2
Requires:   dbus
Requires:   libsoup
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
#BuildRequires:  pkgconfig(gconf-2.0)
BuildRequires:  pkgconfig(libsoup-2.4)
#BuildRequires:  gobject-introspection-devel
#BuildRequires:  vala


%description
GSSDP implements resource discovery and announcement over SSDP and is part
of gUPnP.  GUPnP is an object-oriented open source framework for creating
UPnP devices and control points, written in C using GObject and libsoup.
The GUPnP API is intended to be easy to use, efficient and flexible. GSSDP
implements resource discovery and announcement over SSDP.

%package devel
Summary:    Development package for gssdp
Group:      Development/Libraries
LICENSE:    LGPL-2.0+LICENSE:    LGPL-2.0+
Requires:   %{name} = %{version}-%{release}

%description devel
Development files for gssdp.

%prep
%setup -q -n %{name}-%{version}

%build
%configure --prefix=/usr --enable-introspection=no --enable-gtk-doc-html=no
 
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install
rm -rf %{buildroot}/usr/share/
mkdir -p %{buildroot}/usr/share/license
cp COPYING %{buildroot}/usr/share/license/%{name}

%clean
rm -rf %{buildroot}

%post

%postun

%files
%manifest %{name}.manifest
%defattr(-,root,root,-)
%doc
%{_libdir}/*.so*
/usr/share/license/%{name}

%files devel
%defattr(-,root,root,-)
/usr/include/gssdp-1.0/*
#%{_libdir}/*.a
%{_libdir}/*.so*
%{_libdir}/pkgconfig/*

