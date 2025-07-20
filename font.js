#!/usr/bin/env node
'use strict';

const efm = require('electron-font-manager');
const { getAvailableFontFamilies } = efm;

const availableFonts = getAvailableFontFamilies();
console.log(availableFonts());
