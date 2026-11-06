#!/usr/bin/env bash
set -e

VERSION=$(cat version.txt)
DISTDIR=$PWD/dist
BUILDDIR=$PWD/build/spacecrafts_$VERSION

rm -rf $BUILDDIR
mkdir -p $BUILDDIR
rm -rf $DISTDIR
mkdir -p $DISTDIR

rsync -a CHANGELOG.md $BUILDDIR
rsync -a README.md $BUILDDIR/
rsync -av spacecrafts/ $BUILDDIR

tar -czf $DISTDIR/spacecrafts_${VERSION}.tar.gz -C $(dirname $BUILDDIR) $(basename $BUILDDIR)
