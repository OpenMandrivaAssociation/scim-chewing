%define version	0.3.191
%define release	%mkrel 2

%define chewing_version	        0.3.091
%define scim_version		1.4.5

%define libname_orig lib%{name}
%define libname %mklibname %{name} 0

Name:		scim-chewing
Summary:	SCIM IMEngine module for chewing
Version:	%{version}
Release:	%{release}
Group:		System/Internationalization
License:	GPL
URL:		http://chewing.csie.net/
Source0:	%{name}-%{version}.tar.bz2
Requires:	libchewing >= %{chewing_version}
Requires:	scim >= %{scim_version}
BuildRequires:  libchewing-devel >= %{chewing_version}
BuildRequires:  scim-devel >= %{scim_version}
BuildRequires:  intltool

# compatibility
Obsoletes:	%mklibname %{name} 0
Provides:	%mklibname %{name} 0

%description
Scim-chewing is an SCIM IMEngine module for chewing,
an intelligent Chinese phonetic input method.


%prep
%setup -q

%build
[ ! -x configure ] && ./bootstrap
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std mkinstalldirs='mkdir -p'

# remove unnecessary files
rm -f %{buildroot}%{_libdir}/scim-1.0/*/*/*.{a,la}

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README
%{_datadir}/scim/icons/*
%{_libdir}/scim-1.0/*/IMEngine/*.so
%{_libdir}/scim-1.0/*/SetupUI/*.so


