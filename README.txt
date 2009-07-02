Introduction
============

P2 is a lightweight, airy theme for Plone 3.0. It features a shadowed logo,
content and footer (for those with recent browsers, otherwise a faint border
is used), elegant san serif fonts, with site and global tabs moved to the
bottom of the page.


Installation
============

Instructions are included in the distribution. In summary: install the egg
from pypi via buildout or easy_install, or download a tarball and run `python
setup.py install`.


Developers notes
================

While theme can be easily generated from a paster template, unfortunately such
themes don't deal with non-trivial uninstallation, which is needed if you move
or hide viewlets as P2 does. Examples being thin on the ground, P2 can serve
as case study for how to sensibly revert moved and hidden viewlets. Also see
the references below.


Credits
=======

Thanks to Thomas Massman and Tobias Schmidt for pointing out the shortcomings
of paster-generated themes.

P2 theme is based on the Wordpress theme of the same name by by `Automattic
<http://automattic.com/>`__.


References
==========

* Plone.org `Reordering and hiding viewlets
  <http://plone.org/documentation/tutorial/customizing-main-template-viewlets/reordering-and-hiding-viewlets>`__

* Weblion.psu.edu `Plone 3 theme uninstall profile
  <https://weblion.psu.edu/trac/weblion/wiki/PloneThreeThemeUninstallProfile>`__

* Weblion.psu.edu `Introduction to viewlets in Plone 3
  <http://weblion.psu.edu/documentation/presentations/ui-and-theming/introduction-to-viewlets-in-plone-3-part-2-of-2/>`__


