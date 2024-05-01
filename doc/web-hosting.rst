===========
Web Hosting
===========

Projects typically need web sites for documentation and other information.

Providers
=========

`GitHub Pages`_
    GitHub pages is usually the best solution for web sites that are static
    HTML. Many people know how to use it, and it is free. It is also easy to
    set up and maintain. They recommend not using it for sites bigger than 1
    Gbyte. You are only allowed static HTML, CSS, and JavaScript files. You
    can use Jekyll to generate the site, but you cannot use server-side
    languages like PHP. You can use client-side JavaScript to make the site
    interactive. You can use a custom domain name, HTTPS, and a custom 404 page.

.. _`GitHub Pages`: https://pages.github.com/

Domain Names
============

Most providers make it easy to host a web site in their domain. For example, the oneapi spec uses GitHub pages and can be found at: https://uxlfoundation.github.io/oneAPI-spec/spec/. While this is fine for many projects, some projects may want to have their own domain name. Using your own domain name gives you more flexibility for future changes. For example, GitHub pages uses their `github.io` domain name, the org name, and the repo name. If any of that changes, you will need to update all the links and set up redirects. If you use your own domain name, you can change the hosting provider without changing the domain name.

Web hosting providers, including GitHub pages, lets you use your own domain name. You can buy a domain name from a domain name registrar, and then set up the DNS to point to the hosting provider. While it is not hard or expensive to do this, you may want to use the uxlfoundation.org domain name:

* Linux foundation owns and manages the uxlfoundation.org domain name.
* Establishes the foundation as the owner of the project.

For an example see the `UXL project site`_ which is hosted on GitHub pages but uses the uxlfoundation.org domain name. It is published from the `UXL project site repo`_.

.. _`UXL project site`: https://uxlfoundation.org/
.. _`UXL project site repo`: https://github.com/uxlfoundation/uxlfoundation.org
