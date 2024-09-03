import { NgModule } from "@angular/core";
import { RouterModule, Routes } from "@angular/router";
import { TabsPage } from "./tabs.page";

const routes: Routes = [
  {
    path: "tabs",
    component: TabsPage,
    children: [
      {
        path: "actors",
        loadChildren: "../actors/actors.module#ActorsPageModule",
      },
      {
        path: "user-page",
        loadChildren: "../user-page/user-page.module#UserPagePageModule",
      },
      {
        path: "movies",
        loadChildren: "../movies/movies.module#MoviesPageModule",
      },
      {
        path: "",
        redirectTo: "/tabs/actors",
        pathMatch: "full",
      },
    ],
  },
  {
    path: "",
    redirectTo: "/tabs/actors",
    pathMatch: "full",
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class TabsPageRoutingModule {}
