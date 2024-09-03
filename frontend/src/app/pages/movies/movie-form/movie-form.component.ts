import { Component, OnInit, Input } from "@angular/core";
import { Movie, MoviesService } from "src/app/services/movies.service";
import { ModalController } from "@ionic/angular";
import { AuthService } from "src/app/services/auth.service";

@Component({
  selector: "app-movie-form",
  templateUrl: "./movie-form.component.html",
  styleUrls: ["./movie-form.component.scss"],
})
export class MovieFormComponent implements OnInit {
  @Input() movie: Movie;
  @Input() isNew: boolean;

  constructor(
    public auth: AuthService,
    private modalCtrl: ModalController,
    private moviesService: MoviesService
  ) {}

  ngOnInit() {
    if (this.isNew) {
      this.movie = {
        id: -1,
        title: "",
        release_date: "",
      };
    }
  }

  customTrackBy(index: number, obj: any): any {
    return index;
  }

  closeModal() {
    this.modalCtrl.dismiss();
  }

  saveClicked() {
    this.moviesService.saveMovie(this.movie);
    this.closeModal();
  }

  deleteClicked() {
    this.moviesService.deleteMovie(this.movie);
    this.closeModal();
  }
}
