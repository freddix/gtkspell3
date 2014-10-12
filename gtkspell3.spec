Summary:	GtkTextView widget for GTK+3
Name:		gtkspell3
Version:	3.0.6
Release:	1
License:	GPL
Group:		X11/Libraries
Source0:	http://gtkspell.sourceforge.net/download/%{name}-%{version}.tar.gz
# Source0-md5:	cdc550a06dc424c8c497672bc54649db
URL:		http://gtkspell.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	docbook-dtd42-xml
BuildRequires:	enchant-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk+3-devel
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	vala-vapigen
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GtkSpell provides MSWord/MacOSX-style highlighting of misspelled words
in a GtkTextView widget. Right-clicking a misspelled word pops up a
menu of suggested replacements.

%package devel
Summary:	Header files for gtkspell
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	enchant-devel

%description devel
Header files for gtkspell.

%package apidocs
Summary:	gtkspell API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
gtkspell API documentation.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__gtkdocize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{ak,son}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_libdir}/girepository-1.0/GtkSpell-3.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/gtkspell-3.0
%{_pkgconfigdir}/*.pc
%{_datadir}/gir-1.0/GtkSpell-3.0.gir
%{_datadir}/vala/vapi/gtkspell3-3.0.deps
%{_datadir}/vala/vapi/gtkspell3-3.0.vapi

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}

