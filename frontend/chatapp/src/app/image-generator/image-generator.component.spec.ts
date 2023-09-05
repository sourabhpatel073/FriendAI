import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ImageGeneratorComponent } from './image-generator.component';

describe('ImageGeneratorComponent', () => {
  let component: ImageGeneratorComponent;
  let fixture: ComponentFixture<ImageGeneratorComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ImageGeneratorComponent]
    });
    fixture = TestBed.createComponent(ImageGeneratorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
