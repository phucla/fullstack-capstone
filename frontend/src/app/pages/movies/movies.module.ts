import { NgModule } from "@angular/core";
import { CommonModule } from "@angular/common";
import { FormsModule } from "@angular/forms";
import { Routes, RouterModule } from "@angular/router";

import { IonicModule } from "@ionic/angular";

import { MoviesPage } from "./movies.page";
import { MovieGraphicComponent } from "./movie-graphic/movie-graphic.component";
import { MovieFormComponent } from "./movie-form/movie-form.component";

const routes: Routes = [
  {
    path: "",
    component: MoviesPage,
  },
];

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    RouterModule.forChild(routes),
  ],
  entryComponents: [MovieFormComponent],
  declarations: [MoviesPage, MovieGraphicComponent, MovieFormComponent],
})
export class MoviesPageModule {}
