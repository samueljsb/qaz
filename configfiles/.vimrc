" Vundle
set nocompatible
filetype off

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'

" Plugins
Plugin 'itchyny/lightline.vim'
Plugin 'editorconfig/editorconfig-vim'
Plugin 'tomasiser/vim-code-dark'

call vundle#end()

" lightline
set laststatus=2

syntax on
:set mouse=a

colorscheme codedark

" Wrap gitcommit file types at the appropriate length
filetype indent plugin on

" spelling
:set spell
