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
        children: [
          {
            path: "",
            children: [
              {
                path: "",
                loadChildren: "../actors/actors.module#ActorsPageModule",
                pathMatch: "full",
              },
              {
                path: "",
                redirectTo: "/tabs/actors",
                pathMatch: "full",
              },
            ],
          },
        ],
      },
      {
        path: "user-page",
        children: [
          {
            path: "",
            children: [
              {
                path: "",
                loadChildren:
                  "../user-page/user-page.module#UserPagePageModule",
                pathMatch: "full",
              },
              {
                path: "",
                redirectTo: "/tabs/user-page",
                pathMatch: "full",
              },
            ],
          },
        ],
      },
      {
        path: "movies",
        children: [
          {
            path: "",
            children: [
              {
                path: "",
                loadChildren: "../movies/movies.module#MoviesPageModule",
                pathMatch: "full",
              },
              {
                path: "",
                redirectTo: "/tabs/movies",
                pathMatch: "full",
              },
            ],
          },
        ],
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
