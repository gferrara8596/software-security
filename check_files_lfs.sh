#!/bin/bash

# Trova tutti i file nella repository con dimensione maggiore di 49MB
large_files=$(find . -type f -size +49M)

# Traccia i file trovati con Git LFS
for file in $large_files; do
  git lfs track "$file"
done

