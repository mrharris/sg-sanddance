import React from "react";
import ReactDOM from "react-dom";

import "@msrvida/sanddance-explorer/dist/css/sanddance-explorer.css";
import * as deck from "@deck.gl/core";
import * as layers from "@deck.gl/layers";
import * as luma from "luma.gl";
import * as fabric from "office-ui-fabric-react";
import * as vega from "vega";
import {Explorer, use} from "@msrvida/sanddance-explorer";
import "./styles.css";

fabric.initializeIcons();

use(fabric, vega, deck, layers, luma);

const data = [
  { a: 1, b: "c1", c: 10 },
  { a: 1, b: "c2", c: 20 },
  { a: 2, b: "c3", c: 30 },
  { a: 3, b: "c4", c: 40 }
];

function get_data() {
    let el = document.getElementById("app");
    return JSON.parse(JSON.parse(el.dataset.entities));
}

const explorerProps = {
  logoClickUrl: "https://microsoft.github.io/SandDance/",
  mounted: explorer => {
    explorer.load(get_data());
  }
};

ReactDOM.render(
  <Explorer {...explorerProps} />,
  document.getElementById("app")
);
