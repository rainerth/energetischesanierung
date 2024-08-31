# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
# https://sphinx-tutorial.readthedocs.io/
# https://www.sphinx-doc.org/en/master/index.html
# https://www.sphinx-doc.org/en/master/usage/theming.html#builtin-themes
# https://docutils.sourceforge.io/docs/ref/rst/directives.html#list-table

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
from datetime import datetime
from os import environ

sys.path.append(os.path.abspath("./_ext"))

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
	'sphinx.ext.imgconverter',
	'sphinx.ext.graphviz',
	'sphinx.ext.todo',
	'sphinx.ext.githubpages',
]

intersphinx_mapping = {
	'hasecke': ('https://softwaredocumentation.blob.core.windows.net/haseckesphinxbuch/html/', None),
}

# Add additional config values
# https://latex-programming.fandom.com/wiki/List_of_LaTeX_symbols

def setup(app):
	from sphinx.util.texescape import tex_replacements
	tex_replacements += [(u'♮', u'$\\natural$'),
						 (u'ē', u'\\=e'),
						 (u'♩', u'\\quarternote'),
						 (u'↑', u'$\\uparrow$'),
						 (u'❌',u'X'),
						 (u'❗',u' !! '),
						 (u'▸', u'$\\triangleright$'),
						 (u'➥', u'$\\rightarrow$'),
						 (u'±',u'$\\pm$'),
						 (u'α', u'$\\alpha$'),
						 (u'β', u'$\\beta$'),
						 (u'γ', u'$\\gamma$'),
						 (u'Δ', u'$\\delta$'),
						 (u'™', u'$\\textsuperscript{TM}$')
						]
	app.add_config_value('releaselevel', '', True)


# -- Project information -----------------------------------------------------
# The full version, including alpha/beta/rc tags
release = '2024-04'
today_fmd = '%d-%m-%Y'


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'EnergetischeSanierung'
projectname = 'Energetische Sanierung'
copyright = '2024, Rainer Thieringer | Creative Commons Lizenz 4.0 (BY-NC-SA 4.0)'
author = 'Rainer Thieringer'


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'de'
languagecode = str(os.getenv("LANGCODE"))

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
# excluding _inc.rst avoids double parsing errors of included rst files.
# Name those files abcdef.inc.rst

smartquotes = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'nature'
# html_theme = 'classic'
# html_theme = 'sphinx_book_theme'
# html_theme = "sphinx_rtd_theme"
# panels_add_bootstrap_css = False
html_theme = 'furo'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
# html_logo = '_static/wappen_thieringer.png'
# html_favicon = "_static/trumpf_logo.ico"

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
	'css/trumpf.css',
]

# -- Latex
# https://www.sphinx-doc.org/en/master/latex.html
# https://newbedev.com/package-inputenc-error-unicode-char-u8-b-not-set-up-for-use-with-latex


# https://docs.readthedocs.io/en/stable/guides/manage-translations.html#using-transifex

locale_dirs = ['./_locales']

# https://tug.org/FontCatalogue/

# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-latex-output
# https://www.sphinx-doc.org/en/master/latex.html
# https://docs.readthedocs.io/en/stable/guides/pdf-non-ascii-languages.html
latex_engine = 'xelatex'

latex_documents = [
	('index', project  + '_' + languagecode + '.tex', projectname + ' (' + project + ')', author, 'manual'),
]

latex_elements = {
	'utf8extra': '',
	'papersize': 'a4paper',
	'extraclassoptions': 'openany,oneside',
	'pointsize': '11pt',
	'figure_align': 'H',
	'fontpkg': r'''
		\usepackage{fontspec}
		\setlength{\headheight}{13.8pt}
		\setmainfont{Gillius ADF}
		\setmonofont{FreeMono}
	''',

	'preamble': r'''
		%%%add number to subsubsection 2=subsection, 3=subsubsection
		%%% below subsubsection is not good idea.
		\setcounter{secnumdepth}{3}
		%
		%%%% Table of content upto 2=subsection, 3=subsubsection
		\setcounter{tocdepth}{2}

		\usepackage{polyglossia}
		\setmainlanguage{german}
		\setotherlanguage{english}

		\usepackage{microtype}
		\usepackage{amsmath,amsfonts,amssymb,amsthm}
		\usepackage{graphicx}

		\renewcommand*\sfdefault{ugq}

		%%% reduce spaces for Table of contents, figures and tables
		%%% it is used "\addtocontents{toc}{\vskip -1.2cm}" etc. in the document

		\usepackage{color}
		\usepackage{transparent}
		\usepackage{eso-pic}
		\usepackage{lipsum}


		%% spacing between line
		\usepackage{setspace}
		%%%%\onehalfspacing
		%%%%\doublespacing
		\singlespacing

		%%%%%%%%%%% datetime
		\usepackage{datetime}
		\newdateformat{MonthYearFormat}{\monthname[\THEMONTH], \THEYEAR}

		%%% page number
		\fancyfoot[CO, CE]{\thepage}

		\renewcommand{\headrulewidth}{0.5pt}
		\renewcommand{\footrulewidth}{0.5pt}

		\RequirePackage{tocbibind} %%% comment this to remove page number for following
		\addto\captionsenglish{\renewcommand{\contentsname}{Table of contents}}
		\addto\captionsenglish{\renewcommand{\listfigurename}{List of figures}}
		\addto\captionsenglish{\renewcommand{\listtablename}{List of tables}}
		% \addto\captionsenglish{\renewcommand{\chaptername}{Chapter}}

		%%reduce spacing for itemize
		%%\usepackage{enumitem}
		%%\setlist{nosep}

		%%%%%%%%%%% Quote Styles at the top of chapter
		\usepackage{epigraph}
		\setlength{\epigraphwidth}{0.8\columnwidth}
		\newcommand{\chapterquote}[2]{\epigraphhead[60]{\epigraph{\textit{#1}}{\textbf {\textit{--#2}}}}}
		%%%%%%%%%%% Quote for all places except Chapter
		\newcommand{\sectionquote}[2]{{\quote{\textit{``#1''}}{\textbf {\textit{--#2}}}}}

		\usepackage[default]{gillius}
		\usepackage{enumitem}\setlistdepth{99}

		\setlength{\tymin}{40pt}
		\setlength{\tabcolsep}{1.2em}
		\renewcommand{\arraystretch}{1.5}

		\usepackage[titles]{tocloft}
		\cftsetpnumwidth {1.25cm}\cftsetrmarg{1.5cm}
		\setlength{\cftchapnumwidth}{1.75cm}
		\setlength{\cftsecindent}{\cftchapnumwidth}
		\setlength{\cftsecnumwidth}{2.25cm}

		\usepackage{array}
		\usepackage{colortbl}
		\setlength\extrarowheight{2pt}
		\renewcommand{\arraystretch}{1.5}  % Etwas mehr Platz zwischen den Zeilen
		\usepackage{makecell}
		\renewcommand\theadalign{lt}  % Kopfzeilen links oben ausrichten
		\renewcommand\cellalign{lt}   % Zelleninhalte links oben ausrichten
		\let\oldtabular\tabular
		\let\endoldtabular\endtabular
		\renewenvironment{tabular}{\oldtabular}{\endoldtabular\arrayrulecolor{white}}



	''',

	# Latex figure (float) alignment
	#
	# 'figure_align': 'htbp',
	'sphinxsetup': \
		'hmargin={1in,1in}, vmargin={1.25in,1.25in}, \
		verbatimwithframe=true, \
		TitleColor={rgb}{0,0,0}, \
		HeaderFamily=\\rmfamily\\bfseries, \
		InnerLinkColor={rgb}{0,0,1}, \
		OuterLinkColor={rgb}{0,0,1}',
	'printindex': r'\footnotesize\raggedright\printindex',

}


# https://docs.readthedocs.io/en/stable/guides/manage-translations.html#using-transifex
gettext_uuid = True
gettext_compact = False


# usage of environment variables for builds:
# $ export DOCSCOPE=production; make clean; make html; unset DOCSCOPE
# Windows:
# set DOCSCOPE=panelpc
# make clean
# make html
# set DOCSCOPE=
docscope = os.getenv('DOCSCOPE') or 'public'

# https://www.sphinx-doc.org/en/master/usage/configuration.html#module-conf
# https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#including-content-based-on-tags
# Only tags set via the -t command-line option or via tags.add('tag') can be queried
# using tags.has('tag'). Note that the current builder tag is not available in conf.py,
# as it is created after the builder is initialized.
tags.add(docscope)

exclude_patterns = [
	'_build', 'Thumbs.db', '.DS_Store', '_input', 'node_modules'
]
releaselevelstring = project

if docscope == 'internal' or docscope == 'public':
	releases_debug = True

	exclude_patterns = [
		'_build', 'Thumbs.db', '.DS_Store', '_input', 'node_modules',
		'build-helpers', '**/nnnn', '**.inc.rst', 'README*.md'
	]
	todo_include_todos = True

	releaselevelstring =  project + ' !!! Ohne Gewähr und noch in Arbeit !!!'

	# https://sphinx-book-theme.readthedocs.io/en/latest/customize/sidebar-primary.html

else:
	# Release Setting, activate this to test for no warnings with ``make clean html``  before git push
	exclude_patterns = [
		'_build', 'Thumbs.db', '.DS_Store', '_input', 'node_modules',
		'**/nnnn', '**.inc.rst',
		'99*', '_static/code'
	]
	todo_include_todos = False

	releases_release_uri = ''
	releases_issue_uri = ''
	releases_debug = False

	# https://sphinx-book-theme.readthedocs.io/en/latest/customize/sidebar-primary.html



# Global text replacements
# https://unicode-table.com/en/sets/arrow-symbols/
# https://symbl.cc/en/collections/numerals/

rst_epilog = u"""
.. |copy| unicode:: 0xA9  .. copyright sign
.. |checkmark| unicode:: 0x2714  .. ✔
.. |crossmark| unicode:: 0x274C  .. ❌
.. |important| unicode:: 0x2757  .. ❗
.. |step| unicode:: 0x25B8  .. ▸
.. |arrow| unicode:: 0x27A5  .. ➥
.. |U1w| unicode:: 0x2780  ..  ➀
.. |U2w| unicode:: 0x2781  ..  ➁
.. |U3w| unicode:: 0x2782  ..  ➂
.. |U4w| unicode:: 0x2783  ..  ➃
.. |U5w| unicode:: 0x2784  ..  ➄
.. |U6w| unicode:: 0x2785  ..  ➅
.. |U7w| unicode:: 0x2786  ..  ➆
.. |U8w| unicode:: 0x2787  ..  ➇
.. |U9w| unicode:: 0x2788  ..  ➈
.. |U10w| unicode:: 0x2789  ..  ➉

.. |U1b| unicode:: 0x278A  ..  ➊
.. |U2b| unicode:: 0x278B  ..  ➋
.. |U3b| unicode:: 0x278C  ..  ➌
.. |U4b| unicode:: 0x278D  ..  ➍
.. |U5b| unicode:: 0x278E  ..  ➎
.. |U6b| unicode:: 0x278F  ..  ➏
.. |U7b| unicode:: 0x2790  ..  ➐
.. |U8b| unicode:: 0x2791  ..  ➑
.. |U9b| unicode:: 0x2792  ..  ➒
.. |U10b| unicode:: 0x2793  ..  ➓

.. |WASTEBASKET| unicode:: 0x1F5D1  .. 🗑


""".format(
		datetime.now().strftime(today_fmd),
		releaselevelstring
	)

