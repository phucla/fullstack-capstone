import { Component, OnInit, Input } from "@angular/core";
import { Movie } from "src/app/services/movies.service";

@Component({
  selector: "app-movie-graphic",
  templateUrl: "./movie-graphic.component.html",
  styleUrls: ["./movie-graphic.component.scss"],
})
export class MovieGraphicComponent implements OnInit {
  @Input() movie: Movie;

  constructor() {}

  ngOnInit() {}
}
