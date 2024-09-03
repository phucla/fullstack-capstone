import { CUSTOM_ELEMENTS_SCHEMA } from "@angular/core";
import { async, ComponentFixture, TestBed } from "@angular/core/testing";

import { MovieGraphicComponent } from "./movie-graphic.component";

describe("MovieGraphicComponent", () => {
  let component: MovieGraphicComponent;
  let fixture: ComponentFixture<MovieGraphicComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [MovieGraphicComponent],
      schemas: [CUSTOM_ELEMENTS_SCHEMA],
    }).compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MovieGraphicComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it("should create", () => {
    expect(component).toBeTruthy();
  });
});
