===
dot
===

... --- ... for your dotfiles.

Why
===

Do you use lots of programs? Do you like to customize? Do you use
several machines for work and play? Well, you already know why.

Usage
=====

Something like:

.. code:: bash

    dot config --repo=https://github.com/dustinrc/dotfiles.git
    dot pull
    dot add --name=vim ~/.vimrc ~/.vim
    dot diff
    dot commit vim
    dot push
    dot use bashrc
    sudo dot use --location=/etc/ntp.conf ntp:ntp.conf

Or, very simply:

.. code:: bash

    dot config --repo=https://github.com/dustinrc/dotfiles
    dot pull
    dot use
    dot add .config
    dot commit
    dot push

TODO
====

*Everything...*

