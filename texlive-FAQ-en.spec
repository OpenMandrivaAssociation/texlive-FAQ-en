Name:		texlive-FAQ-en
Version:	3.23
Release:	1
Summary:	A compilation of Frequently Asked Questions with answers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive//help/uk-tex-faq
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/FAQ-en.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/FAQ-en.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
The FAQ that has in the past been published in the UK TeX Users
Group journal Baskerville (though updated more frequently on
CTAN). It is also available (and searchable) on the web.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/generic/FAQ-en/CHANGES-3.16b
%doc %{_texmfdistdir}/doc/generic/FAQ-en/CHANGES-3.16c
%doc %{_texmfdistdir}/doc/generic/FAQ-en/CHANGES-3.17
%doc %{_texmfdistdir}/doc/generic/FAQ-en/CHANGES-3.18
%doc %{_texmfdistdir}/doc/generic/FAQ-en/CHANGES-3.19
%doc %{_texmfdistdir}/doc/generic/FAQ-en/CHANGES-3.19a
%doc %{_texmfdistdir}/doc/generic/FAQ-en/CHANGES-3.19c
%doc %{_texmfdistdir}/doc/generic/FAQ-en/CHANGES-3.19d
%doc %{_texmfdistdir}/doc/generic/FAQ-en/CHANGES-3.20
%doc %{_texmfdistdir}/doc/generic/FAQ-en/CHANGES-3.21
%doc %{_texmfdistdir}/doc/generic/FAQ-en/CHANGES-3.22
%doc %{_texmfdistdir}/doc/generic/FAQ-en/CHANGES-3.23
%doc %{_texmfdistdir}/doc/generic/FAQ-en/ChangeLog
%doc %{_texmfdistdir}/doc/generic/FAQ-en/FAQ-html.tar.gz
%doc %{_texmfdistdir}/doc/generic/FAQ-en/Makefile
%doc %{_texmfdistdir}/doc/generic/FAQ-en/README
%doc %{_texmfdistdir}/doc/generic/FAQ-en/archive.cfg
%doc %{_texmfdistdir}/doc/generic/FAQ-en/dirctan.tex
%doc %{_texmfdistdir}/doc/generic/FAQ-en/faq-adj-types.tex
%doc %{_texmfdistdir}/doc/generic/FAQ-en/faq-backgrnd.tex
%doc %{_texmfdistdir}/doc/generic/FAQ-en/faq-biblio.tex
%doc %{_texmfdistdir}/doc/generic/FAQ-en/faq-bits+pieces.tex
%doc %{_texmfdistdir}/doc/generic/FAQ-en/faq-docs.tex
%doc %{_texmfdistdir}/doc/generic/FAQ-en/faq-dvi.tex
%doc %{_texmfdistdir}/doc/generic/FAQ-en/faq-fmt-conv.tex
%doc %{_texmfdistdir}/doc/generic/FAQ-en/faq-fonts.tex
%doc %{_texmfdistdir}/doc/generic/FAQ-en/faq-getit.tex
%doc %{_texmfdistdir}/doc/generic/FAQ-en/faq-graphics.tex
%doc %{_texmfdistdir}/doc/generic/FAQ-en/faq-how-do-i.tex
%doc %{_texmfdistdir}/doc/generic/FAQ-en/faq-hyp+pdf.tex
%doc %{_texmfdistdir}/doc/generic/FAQ-en/faq-install.tex
%doc %{_texmfdistdir}/doc/generic/FAQ-en/faq-intro.tex
%doc %{_texmfdistdir}/doc/generic/FAQ-en/faq-jot-err.tex
%doc %{_texmfdistdir}/doc/generic/FAQ-en/faq-lab-ref.tex
%doc %{_texmfdistdir}/doc/generic/FAQ-en/faq-litprog.tex
%doc %{_texmfdistdir}/doc/generic/FAQ-en/faq-mac-prog.tex
%doc %{_texmfdistdir}/doc/generic/FAQ-en/faq-projects.tex
%doc %{_texmfdistdir}/doc/generic/FAQ-en/faq-support.tex
%doc %{_texmfdistdir}/doc/generic/FAQ-en/faq-symbols.tex
%doc %{_texmfdistdir}/doc/generic/FAQ-en/faq-t-g-wr.tex
%doc %{_texmfdistdir}/doc/generic/FAQ-en/faq-texsys.tex
%doc %{_texmfdistdir}/doc/generic/FAQ-en/faq-the-end.tex
%doc %{_texmfdistdir}/doc/generic/FAQ-en/faq-wdidt.tex
%doc %{_texmfdistdir}/doc/generic/FAQ-en/faq.cls
%doc %{_texmfdistdir}/doc/generic/FAQ-en/faq.sty
%doc %{_texmfdistdir}/doc/generic/FAQ-en/faqfont.cfg
%doc %{_texmfdistdir}/doc/generic/FAQ-en/faqfont.cfg.cmfonts
%doc %{_texmfdistdir}/doc/generic/FAQ-en/faqfont.cfg.lmfonts
%doc %{_texmfdistdir}/doc/generic/FAQ-en/faqfont.cfg.mbvj
%doc %{_texmfdistdir}/doc/generic/FAQ-en/faqfont.cfg.ugm
%doc %{_texmfdistdir}/doc/generic/FAQ-en/filectan.tex
%doc %{_texmfdistdir}/doc/generic/FAQ-en/gather-faqbody.tex
%doc %{_texmfdistdir}/doc/generic/FAQ-en/letterfaq.pdf
%doc %{_texmfdistdir}/doc/generic/FAQ-en/letterfaq.tex
%doc %{_texmfdistdir}/doc/generic/FAQ-en/locations.mk
%doc %{_texmfdistdir}/doc/generic/FAQ-en/markup-syntax
%doc %{_texmfdistdir}/doc/generic/FAQ-en/newfaq.pdf
%doc %{_texmfdistdir}/doc/generic/FAQ-en/newfaq.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
