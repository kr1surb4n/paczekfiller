#!/bin/bash

if [[ ! -v $PACZEK_FILLINGS ]]; then
    export PACZEK_FILLINGS="$HOME/.coat/paczki"
fi

paczek_path=$( find $PACZEK_FILLINGS -type f | fzf )

case $paczek_path in
    *.tpl)
        paczekfiller $paczek_path > ${paczek_path:0:-4};;
        *)
        cp $paczek_path $(basename $paczek_path);;
esac
