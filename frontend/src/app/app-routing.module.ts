import { NgModule } from "@angular/core";
import { PreloadAllModules, RouterModule, Routes } from "@angular/router";
import { TabsPage } from "./pages/tabs/tabs.page";

const routes: Routes = [
  {
    path: "",
    redirectTo: "/actors",
    pathMatch: "full",
  },
  {
    path: "actors",
    children: [
      {
        path: "",
        children: [
          {
            path: "",

            loadChildren: "./pages/actors/actors.module#ActorsPageModule",
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
              "./pages/user-page/user-page.module#UserPagePageModule",
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
            loadChildren: "./pages/movies/movies.module#MoviesPageModule",
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
];
@NgModule({
  imports: [
    RouterModule.forRoot(routes, { preloadingStrategy: PreloadAllModules }),
  ],
  exports: [RouterModule],
})
export class AppRoutingModule {}
