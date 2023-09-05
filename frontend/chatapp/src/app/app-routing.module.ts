import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { SignupComponent } from './signup/signup.component';
import { HomeComponent } from './home/home.component';
import { ProfileComponent } from './profile/profile.component';
import { ChatHistoryListComponent } from './chat-history-list/chat-history-list.component';
import { ChatDetailsComponent } from './chat-details/chat-details.component';
import { GeneralChatComponent } from './general-chat/general-chat.component';
import { ImageGeneratorComponent } from './image-generator/image-generator.component';
import { AuthGuard } from './auth.guard';

const routes: Routes = [
  { path: '', redirectTo: '/login', pathMatch: 'full' },
  { path: 'login', component: LoginComponent },
  { path: 'signup', component: SignupComponent },
  { path: 'home', component: HomeComponent },
  { path: 'chats', component:ChatHistoryListComponent , canActivate: [AuthGuard] },
  { path: 'profile', component: ProfileComponent , canActivate: [AuthGuard] },
  { path: 'general', component: GeneralChatComponent },
  { path: 'chat/:id', component: ChatDetailsComponent },
  { path: 'image', component: ImageGeneratorComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
