%global octpkg image-acquisition

Summary:	Capture images from connected devices with Octave)
Name:		octave-image-acquisition
Version:	0.3.2
Release:	1
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/image-acquisition/
Source0:	https://github.com/Andy1978/octave-image-acquisition/archive/refs/tags/image-acquisition-%{version}.tar.gz

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
%autosetup -p1 -n %{name}-%{octpkg}-%{version}

%build
%set_build_flags
export CXXFLAGS="%optflags `pkg-config --cflags cairo`"
pushd src
autoreconf -fiv
popd
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

