import { Component, OnInit, Input } from "@angular/core";
import { Actor, ActorsService } from "src/app/services/actors.service";
import { ModalController } from "@ionic/angular";
import { AuthService } from "src/app/services/auth.service";

@Component({
  selector: "app-actor-form",
  templateUrl: "./actor-form.component.html",
  styleUrls: ["./actor-form.component.scss"],
})
export class ActorFormComponent implements OnInit {
  @Input() actor: Actor;
  @Input() isNew: boolean;

  constructor(
    public auth: AuthService,
    private modalCtrl: ModalController,
    private actorsService: ActorsService
  ) {}

  ngOnInit() {
    if (this.isNew) {
      this.actor = {
        id: -1,
        name: "",
        age: 0,
        gender: "",
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
    this.actorsService.saveActor(this.actor);
    this.closeModal();
  }

  deleteClicked() {
    this.actorsService.deleteActor(this.actor);
    this.closeModal();
  }
}
