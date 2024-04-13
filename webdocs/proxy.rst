.. image:: ./images/gsas2.png
   :scale: 25 %
   :alt: GSAS-II logo
   :align: right
	   
.. index:: Web proxy setup

====================================
Web Proxies
====================================

Some institutions route web traffic between their site and the internet via a special router usually called a `web proxy or a proxy server <https://en.wikipedia.org/wiki/Proxy_server>`_.  If this is the case, the proxy settings have probably been set for your computer or web browser when the computer was initially set up and you may not know it is present, but it will interfere when trying to install GSAS-II or with some of the actions that GSAS-II uses, for example, when updating from GitHub, when accessing a web-based software service, such as ISODISTORT or the Bilboa Crystallographic Server.

Note that the information here may not be completely accurate, as I do not have direct access to an environment with a web proxy where I can test this. 

* *Do I have a proxy*: 
   I have found that at some sites, even many of the IT support people don't know that a web proxy is needed. A web page that can help you check if a proxy is https://www.whatismyip.com/proxy-check. (Previously, I used http://www.whatismyproxy.com/, but Argonne now blocks this as malicious; perhaps so.) A longer informative discussion on how to look for proxy settings for Windows and MacOS can be found here: https://www.linkedin.com/pulse/how-find-proxy-server-address-comprehensive-p6klf/. For Mac/Linux, check the ``http_proxy`` and ``HTTP_PROXY``  environment variable settings.

* *Configuring a proxy*: 
   Once you have determined the name of your proxy, or its IP address and port, you will need a command like this::
  
     git config --global http.proxy http://myproxy:port

   so that git can install and update GSAS-II. Note that  ``myproxy`` will be something like  ``proxyserver.myplace.edu``, or an IP address, like ``10.10.1.10`` and ``port`` will be a number such as ``8080``. This command only needs to be done once. The setting is stored for future reuse. 

   Also, GSAS-II does use the web to access a number of services. Examples being ISODISTORT and Bilboa, as mentioned above, but also to download the data files needed for tutorials and potentially for installing binary files needed for GSAS-II in the ``gitstrap.py`` process. This requires setting the ``HTTP_PROXY``  environment variables. For windows, use these commands::

     set http_proxy=myproxy:port
     set https_proxy=myproxy:port

   these commands can be placed inside the GSAS-II.bat file that was created during the installation process by the ``makeBat.py`` script (but remember to do this every time that you reinstall.)

   For Linux/MacOS, use these commands::

     export HTTP_PROXY=myproxy:port
     export HTTPS_PROXY=myproxy:port

   These are best placed inside your ``~/.profile`` or ``~/.zprofile`` files, but do not take affect until you login or create a new terminal session.

   If you use the `gsas2pkg installer <install.html#gsas2pkg-conda-package>`_,  or the few places in the GSAS-II code where conda packages may be installed, you will need to also provide the following two commands::

     conda config --set proxy_servers.http http://myproxy:port
     conda config --set proxy_servers.https https://myproxy:port

   This command only needs to be done once. The setting is stored for future reuse. 

   GSAS-II can also call Python's built-in pip installer, but this is unlikely to happen (used for exports to OriginPro). For this the configuration command is::

     python -m pip config set global.proxy http://myproxy:port

   This command also only needs to be done once. The setting is stored for future reuse. 

If you are not sure how to do any of the above, I suggest getting help from your local IT support people. It is the least they can do in exchange for making your life difficult with the proxy server.
