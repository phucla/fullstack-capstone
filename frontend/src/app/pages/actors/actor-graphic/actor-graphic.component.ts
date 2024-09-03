import { Component, OnInit, Input } from "@angular/core";
import { Actor } from "src/app/services/actors.service";

@Component({
  selector: "app-actor-graphic",
  templateUrl: "./actor-graphic.component.html",
  styleUrls: ["./actor-graphic.component.scss"],
})
export class ActorGraphicComponent implements OnInit {
  @Input() actor: Actor;

  constructor() {}

  ngOnInit() {}
}
