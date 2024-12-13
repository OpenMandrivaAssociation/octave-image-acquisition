%global octpkg image-acquisition

Summary:	Capture images from connected devices with Octave)
Name:		octave-image-acquisition
Version:	0.2.6
Release:	1
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/image-acquisition/
Source0:	https://downloads.sourceforge.net/octave/image-acquisition-%{version}.tar.gz
# (upstream) https://savannah.gnu.org/bugs/index.php?63136
Patch0:		image-acquisition-0.2.2-octave6.patch

BuildRequires:	octave-devel >= 3.8.0
BuildRequires:	fltk-devel
BuildRequires:	pkgconfig(libv4l2)

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
The Octave-forge Image Aquisition package provides functions to capture
images from connected devices.

Currently only v4l2 is supported.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%dir %{octpkglibdir}
%{octpkglibdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

