import { Injectable } from "@angular/core";
import { HttpClient, HttpHeaders } from "@angular/common/http";

import { AuthService } from "./auth.service";
import { environment } from "src/environments/environment";

export interface Movie {
  id: number;
  title: string;
  release_date: string;
}

@Injectable({
  providedIn: "root",
})
export class MoviesService {
  url = environment.apiServerUrl;

  public items: { [key: number]: Movie } = {};

  constructor(private auth: AuthService, private http: HttpClient) {}

  getHeaders() {
    const header = {
      headers: new HttpHeaders().set(
        "Authorization",
        `Bearer ${this.auth.activeJWT()}`
      ),
    };
    return header;
  }

  getMovies() {
    if (this.auth.can("get:drinks-detail")) {
      this.http
        .get(this.url + "/movies-detail", this.getHeaders())
        .subscribe((res: any) => {
          this.drinksToItems(res.movies);
          console.log(res);
        });
    } else {
      this.http
        .get(this.url + "/movies", this.getHeaders())
        .subscribe((res: any) => {
          this.drinksToItems(res.movies);
          console.log(res);
        });
    }
  }

  saveMovie(movie: Movie) {
    if (movie.id >= 0) {
      // patch
      this.http
        .patch(this.url + "/movies/" + movie.id, movie, this.getHeaders())
        .subscribe((res: any) => {
          if (res.success) {
            this.drinksToItems(res.movies);
          }
        });
    } else {
      // insert
      this.http
        .post(this.url + "/movies", movie, this.getHeaders())
        .subscribe((res: any) => {
          if (res.success) {
            this.drinksToItems(res.movies);
          }
        });
    }
  }

  deleteMovie(movie: Movie) {
    delete this.items[movie.id];
    this.http
      .delete(this.url + "/movies/" + movie.id, this.getHeaders())
      .subscribe((res: any) => {});
  }

  drinksToItems(movies: Array<Movie>) {
    for (const movie of movies) {
      this.items[movie.id] = movie;
    }
  }
}
