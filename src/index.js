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

function get_data() {
    let el = document.getElementById("app");
    return JSON.parse(JSON.parse(el.dataset.entities));
}

const explorerProps = {
  mounted: explorer => {
    explorer.load(get_data());
  }
};

ReactDOM.render(
  <Explorer {...explorerProps} />,
  document.getElementById("app")
);
